<script>
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
        <img src="/images/portrait.png" alt="{title} image">
      </div>
    {/if}
  </div>
</section>

<style>
  section {
    min-height: 80vh;
    border-bottom: 1px solid #eee;
    scroll-margin-top: 4rem;
    display: flex;
    flex-direction: column;
    padding: 10rem 10rem 10rem 13rem;
  }

  h2 {
    margin-top: 0;
  }

  .section-container {
    display: flex;
    width: 100%;
    padding-top: 2rem;
  }

  .left {
    align-items: flex-start;
    text-align: left;
  }

  .right {
    align-items: flex-end;
    text-align: right;
  }

  .with-portrait .text-content {
    flex: 1;
    padding-right: 2rem;
  }

  .with-portrait .image-container {
    flex: 1;
  }

  .text-only .text-content {
    flex: 1;
  }

  .content {
    max-width: 100%;
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
    border-radius: 25px;
  }

   /********************************* Mobile screens (max-width: 640px) *********************************/
  @media (max-width: 1023px) {
    section {
      padding: 0;
    }

    .section-container {
      flex-direction: column;
      align-items: center;
      padding: 0;
    }

    .with-portrait .image-container {
      order: -1; /* Show the image first on mobile */
      padding: 0 0 5rem 0;

    }

    .with-portrait .text-content {
      padding-right: 0;
    }
  }

  /********************************* Desktop and larger screens *********************************/
  @media (min-width: 1024px) {
    .with-portrait .image-container {
      order: 1; /* Show the image on the right on larger screens */
    }

    .with-portrait .text-content {
      order: 0;
    }
  }
</style>