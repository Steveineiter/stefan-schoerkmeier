<script>
  import Section from '$lib/components/Section.svelte';
</script>

<div class="sections-container">
  <Section id="section1" title="Section 1">
    <p>Content for section 1 goes here...</p>
  </Section>

  <Section id="section2" title="Section 2">
    <p>Content for section 2 goes here...</p>
  </Section>

<!--  <Section id="section3" title="Section 3">-->
<!--    <p>Content for section 3 goes here...</p>-->
<!--  </Section>-->
</div>

<style>
  .sections-container {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
</style>
