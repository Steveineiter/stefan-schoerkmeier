<script>
  import Section from '$lib/components/Section.svelte';
  import { sections } from '$lib/sections.js'

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
        <!--TODO import this page / create it as a own file. Because ML page has more sufficticated features in it. Also add the canvas and logic to send pixels to backend yikes-->
        <h1>Foo </h1>
        <p> bar</p>
      {:else}
        <p>{@html section.content}</p>
      {/if}
    </Section>
  {/each}
</div>

<style>
  h1 {
    text-align: center;
  }
</style>
