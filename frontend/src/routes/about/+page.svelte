<script lang="ts">
  // +page.svelte - About Page
</script>

<section class="flex flex-col items-center justify-center text-center bg-surface text-on-surface p-8">
  <!-- Main Heading -->
  <h1 class="text-4xl font-bold">About This Project</h1>

  <!-- Introductory Paragraph -->
  <p class="text-lg text-on-surface/70 mt-4 max-w-3xl">
    Welcome to this demonstration of a modern full‑stack web application. Though streamlined for clarity, it showcases best practices in front‑end design, back‑end APIs, and containerized infrastructure.
  </p>

  <!-- Two-Card Layout -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8 w-full max-w-5xl">
    <!-- Front-End Card -->
    <div class="card p-4">
      <h2 class="text-xl font-semibold mb-2">Front-End</h2>
      <p class="text-base text-on-surface/80">
        Built with <strong>SvelteKit</strong> and styled using <strong>Tailwind CSS</strong> alongside the <strong>Skeleton.dev</strong> UI library. Users can switch between multiple themes and light/dark mode for a flexible, modern interface.
      </p>
    </div>

    <!-- Back-End & Infrastructure Card -->
    <div class="card p-4">
      <h2 class="text-xl font-semibold mb-2">Back-End & Infrastructure</h2>
      <p class="text-base text-on-surface/80">
        Powered by <strong>FastAPI</strong> and <strong>Tortoise ORM</strong> on a <strong>Postgres</strong> database. Real‑time communication is enabled via <strong>WebSockets</strong>, and an <strong>Nginx</strong> reverse proxy manages both HTTP and WebSocket traffic. Everything runs in <strong>Docker Compose</strong> for consistent, reliable deployment.
      </p>
    </div>
  </div>

  <!-- Additional Details & CTA -->
  <p class="text-lg text-on-surface/70 mt-8 max-w-3xl">
    You can submit and vote on feature requests to see the system in action. It includes server-side validation for form requests, instantaneous voting on feature requests using websockets, sorting feature requests in real time.
  </p>

  <a href="/feature_requests" class="btn variant-filled mt-6">
    View Feature Requests
  </a>
</section>
