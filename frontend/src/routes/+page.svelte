<script>
  import Section from '$lib/components/Section.svelte';
  import { sections } from '$lib/sections.js'
  import MachineLearning from './MachineLearning.svelte'

</script>

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
        <MachineLearning color="black" size="4"/>
      {:else}
        <p>{@html section.content}</p>
      {/if}
    </Section>
  {/each}
</div>


