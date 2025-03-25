<script>
  export let id;
  export let title;
</script>

<section {id}>
  <h2>{title}</h2>
  <div class="content">
    <slot></slot>
  </div>
</section>

<style>
  section {
    min-height: 50vh;
    padding: 1rem;
    border-bottom: 1px solid #eee;
    scroll-margin-top: 4rem; /* Add space for the header when scrolling */
  }

  h2 {
    margin-top: 0;
  }
</style>
