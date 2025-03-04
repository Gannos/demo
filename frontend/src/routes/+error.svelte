<!-- src/routes/+error.svelte -->
<script>
  // Provide default values to avoid errors
  export let error = { message: 'An unexpected error occurred' };
  export let status = 500;
</script>

<svelte:head>
  <title>{status === 404 ? 'Page Not Found' : 'Something went wrong'}</title>
</svelte:head>

{#if status === 404}
  <h1 class="text-3xl font-bold text-center">Page Not Found</h1>
  <p class="text-center mt-4">Sorry, we couldn't find the page you're looking for.</p>
{:else}
  <h1 class="text-3xl font-bold text-center">Something went wrong</h1>
  <p class="text-center mt-4">{error.message || 'An unexpected error occurred.'}</p>
{/if}
