<script>
  import { sections } from '$lib/text-data/sections.js'
  import Navbar from "$lib/components/Navbar.svelte";

</script>

<Navbar />

<div class="sections-container">
    {#each sections as section}
        <section id={section.id}>
            <svelte:component
                    this={section.component}
                    title={section.title}
            />
        </section>
    {/each}
</div>


<style>
    section {
    min-height: 80vh;
    border-bottom: 1px solid #eee;
    scroll-margin-top: 4rem;
    display: flex;
    flex-direction: column;
    padding: 10rem 10rem 10rem 13rem;
  }
  /********************************* Mobile screen *********************************/
  @media (max-width: 768px) {
    section {
      padding: 3rem 1.5rem;
    }
  }
</style>
