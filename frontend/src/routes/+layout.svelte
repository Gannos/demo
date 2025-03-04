<script>
  import "../app.css";
  import Navbar from "$lib/components/Navbar.svelte";
</script>

<div>
  <!-- Navbar (Row 1) -->
  <Navbar />

  <!-- Main Content (Row 2) -->
  <main class="grid grid-cols-1 lg:grid-cols-[auto_1fr_auto] gap-4 p-6 h-full">
    <!-- Sidebar (Optional) -->
    <aside class="hidden lg:block bg-surface p-4 rounded-lg h-full">
      <!-- Sidebar content -->
    </aside>

    <!-- Main Content Area -->
    <section class="bg-surface p-2 rounded-lg shadow-lg h-full">
      <slot />
    </section>

    <!-- Extra Section (Optional) -->
    <aside class="hidden md:block max-w-xs bg-surface p-4 rounded-lg h-full">
      <!-- Extra content -->
    </aside>
  </main>
</div>
