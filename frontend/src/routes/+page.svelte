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

      <p>{section.content}</p>
    </Section>
  {/each}
</div>
