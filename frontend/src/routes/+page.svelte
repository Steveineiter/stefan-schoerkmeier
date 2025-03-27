<script>
  import Section from '$lib/components/Section.svelte';
  import { sections } from '$lib/text-data/sections.js'
  import MachineLearning from './MachineLearning.svelte'
  import Navbar from "$lib/components/Navbar.svelte";

</script>

<Navbar />

<div class="sections-container">
  {#each sections as section, i}
    <Section
      id={section.id}
      title={section.title}
      position={i % 2 === 0 ? 'left' : 'right'}
      paddingTop={i === 0 ? "10rem" : "5rem"}
      includePortrait={section.includePortrait}
    >
      {#if section.id === "ml"}
        <MachineLearning color="white" size="1"/>
      {:else}
        <p>{@html section.content}</p>
      {/if}
    </Section>
  {/each}
</div>



