<script lang="ts">
  import { superForm } from 'sveltekit-superforms';
  import { onMount } from 'svelte';
  import SuperDebug from 'sveltekit-superforms';
  
  export let data;
  const { form, errors, enhance } = superForm(data.form);
  console.log("errors: ", $errors);
</script>

<SuperDebug data="{$form}" />
<div class="min-h-screen bg-surface p-8">
  <form
    method="POST"
    use:enhance
    class="w-full max-w-4xl mx-auto space-y-8"
  >
    <h2 class="text-3xl font-bold text-on-surface text-center">
      Submit a Feature Request
    </h2>

    <div class="space-y-2">
      <label for="title" class="block text-lg text-on-surface/80">Title</label>
      <input
        type="text"
        name="title"
        bind:value={$form.title}
        placeholder="Enter feature title"
        class="input w-full border border-on-surface/20 focus:border-primary focus:ring focus:ring-primary/20 rounded-md p-3"
      />
      {#if $errors?.title}
        <p class="text-error-500 text-sm mt-1">{$errors.title}</p>
      {/if}
    </div>

    <div class="space-y-2">
      <label for="description" class="block text-lg text-on-surface/80">Description</label>
      <textarea
        name="description"
        bind:value={$form.description}
        placeholder="Describe your feature request..."
        class="textarea w-full border border-on-surface/20 focus:border-primary focus:ring focus:ring-primary/20 rounded-md p-3"
        rows="6"
      ></textarea>
      {#if $errors?.description}
        <p class="text-error-500 text-sm mt-1">{$errors.description}</p>
      {/if}
    </div>

    <div class="flex justify-end">
      <button type="submit" class="btn variant-filled mt-6">
        Submit
      </button>
    </div>
  </form>
</div>
