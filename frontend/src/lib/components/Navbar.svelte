<script lang="ts">
  import Palette from 'virtual:icons/mdi/palette';
  import Lightbulb from 'virtual:icons/mdi/lightbulb';
  import Octahedron from 'virtual:icons/mdi/octahedron';
  import Hamburger from 'virtual:icons/mdi/hamburger-menu';
  import { AppBar } from '@skeletonlabs/skeleton';
  import { LightSwitch } from '@skeletonlabs/skeleton';

  let themeSelectorOpen = false;

  const themes = [
    "skeleton",
    "wintry",
    "modern",
    "rocket",
    "seafoam",
    "vintage",
    "sahara",
    "hamlindigo",
    "gold-nouveau",
    "crimson"
  ];

  function switchTheme(theme) {
    document.body.setAttribute("data-theme", theme);
    toggleThemeSelector();
  }

  function toggleThemeSelector() {
    themeSelectorOpen = !themeSelectorOpen;
  }
</script>

<!-- Navbar Container -->
<nav class="app-bar bg-primary text-on-primary py-5 px-6 flex justify-between items-center shadow-lg text-lg">

  <!-- Left Section: Logo / Menu -->
  <div class="inline-flex gap-x-6">
    <button type="button" class="text-2xl">
      <a href="/">
        <Octahedron/>
      </a>
    </button>
    <p><a href="/">Home</a></p>
    <p><a href="/about">About</a></p>
    <p><a href="/contact">Contact</a></p>
  </div>

  <!-- Right Section: Theme & Actions -->
  <div class="inline-flex gap-x-6 relative">
    <button type="button" class="text-2xl">
      <LightSwitch class="custom-switch" />
    </button>
    <button on:click={toggleThemeSelector} type="button" class="text-2xl">
      <Palette />
    </button>

    <!-- Dropdown (Theme Selection) -->
  {#if themeSelectorOpen}
    <ul class="absolute right-0 top-full mt-2 bg-tertiary-500/100 text-on-tertiary rounded-lg shadow-lg p-2 w-40 z-50">
      {#each themes as theme}
        <li class="cursor-pointer px-4 py-2 hover:bg-primary/30 rounded-token" on:click={() => switchTheme(theme)}>
          {theme}
        </li>
      {/each}
    </ul>
  {/if}
  </div>
</nav>
