<script lang="ts">
  import ThumbsUp from "virtual:icons/mdi/thumbs-up";
  import ThumbsDown from "virtual:icons/mdi/thumbs-down";
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  export let data;
  export const featureRequests = writable(data.featureRequests);
  const VITE_WEBSOCKET_URL = import.meta.env.VITE_WEBSOCKET_URL;
  let socket;
  onMount(() => {
    socket = new WebSocket(`${VITE_WEBSOCKET_URL}`);
    
    socket.onopen = () => {
      console.log("WebSocket connection established.");
    };

    socket.onmessage = (event) => {
      console.log("Received: ", event.data);
      let response = JSON.parse(event.data);
      if (response['type'] == 'rate') {
        updateRating(response)
      } else {
        console.log("unknown message type");
      }
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed.");
    };
  });

  function updateRating(response) {
    featureRequests.update((requests) =>
      requests
        .map((req) =>
          req.id === response.id ? { ...req, rating: response.rating } : req
        )
        .sort((a, b) => b.rating - a.rating)
    );
}

  function Rate(id, direction) {
    console.log(`Ranking ${direction} item with id ${id}`);
    const message = {
      type: "rate",
      id: id,
      direction: direction
    };
    if (socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify(message));
      console.log("Ranking update sent:", message);
    } else {
      console.error("WebSocket is not open.");
    }
  }
</script>

<section class="container mx-auto px-4 py-8">
  <!-- Header -->
  <div class="flex flex-col sm:flex-row items-center justify-between mb-8">
  <h1 class="text-3xl font-bold text-center w-full">
    Feature Requests
  </h1>
  <a href="/feature_requests/add" class="mt-6 sm:mt-0">
    <button class="btn variant-filled">
      New Request
    </button>
  </a>
</div>

  {#if $featureRequests.length === 0}
    <p class="text-center text-on-surface/70">No feature requests yet.</p>
  {:else}
    <div class="space-y-4 overflow-y-auto max-h-[75vh]">
      {#each $featureRequests as request (request.id)}
  <div class="flex items-center justify-between card p-4 bg-surface shadow-md rounded-lg transition-all duration-300 hover:bg-tertiary-500/50 hover:ring-2 hover:ring-primary/70">
    <div class="flex flex-col items-start space-y-1">
      <h2 class="text-xl font-semibold">{request.title}</h2>
      <p class="text-on-surface/70">{request.description}</p>

    </div>

    <div class="flex flex-col items-center space-y-2">
      <span class="text-sm">{request.created_at}</span>
      <div class="flex items-center gap-1">
        <button on:click={() => Rate(request.id, 'up')} class="p-2">
          <ThumbsUp class="h-5 w-5 hover:text-success-500" />
        </button>
        <button on:click={() => Rate(request.id, 'down')} class="p-2">
          <ThumbsDown class="h-5 w-5 hover:text-error-500" />
        </button>
      </div>
      <span class="text-lg font-bold">{request.rating}</span>
    </div>
  </div>
{/each}
    </div>
  {/if}
</section>
