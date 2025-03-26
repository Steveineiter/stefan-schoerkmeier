<script>
  import testImage from '$lib/images/portrait.png'

  export let id;
  export let title;
  export let paddingTop = "5rem";
  export let position = "left"; // New prop for position
  export let includePortrait = false;
</script>

<section {id} style="padding-top: {paddingTop}">
  <div class="section-container {position} {includePortrait ? 'with-portrait' : 'text-only'}">
    <div class="text-content">
      <h2>{title}</h2>
      <div class="content">
        <slot></slot>
      </div>
    </div>
    {#if includePortrait}
      <div class="image-container">
        <img src={testImage} alt="{title} image">
      </div>
    {/if}
  </div>
</section>

<style>
  section {
    min-height: 80vh;
    padding: 10rem;
    border-bottom: 1px solid #eee;
    scroll-margin-top: 4rem;
    display: flex;
    flex-direction: column;
  }

  h2 {
    margin-top: 0;
  }

  .section-container {
    display: flex;
    width: 100%;
    padding-top: 2rem
  }

  /* Position styles */
  .left {
    align-items: flex-start;
    text-align: left;
  }

  .right {
    align-items: flex-end;
    text-align: right;
  }

  /* Portrait layout styles - now 50/50 split */
  .with-portrait .text-content {
    flex: 1; /* Takes 50% of the space */
    padding-right: 2rem;
  }

  .with-portrait .image-container {
    flex: 1; /* Takes 50% of the space */
  }

  .text-only .text-content {
    flex: 1; /* Takes full width */
  }

  .content {
    max-width: 100%; /* Changed from 60% to allow proper flexbox layout */
  }

  .image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 2rem;
  }

  img {
    max-width: 100%;
    height: auto;
    border-radius: 25px
  }
</style>
