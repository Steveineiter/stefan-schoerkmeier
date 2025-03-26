<script>
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte';
  import { page } from '$app/state';

  const isHomeDir = page.url.pathname === "/"
</script>




<div class="app-container">
  <Header />
  <div class="content-container">
    <main>
      <slot />
    </main>
  </div>
</div>
<Footer />

<style>
  .app-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }

  .content-container {
    display: flex;
    flex: 1;
    overflow: hidden;
  }

  main {
    flex: 1;
    overflow-y: auto;
    scroll-behavior: smooth;
    padding: 1rem;
  }

  :global(body),
  :global(html) {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
</style>
