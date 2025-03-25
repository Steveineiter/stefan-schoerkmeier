<script>
  import { sections } from '$lib/sections.js'
  // const sections = [
  //   { id: 'about', label: 'About' },
  //   { id: 'ml', label: 'Machine Learning' },
  //   // { id: 'section3', label: 'Section 3' },
  // ];

  // Function to scroll to section
  function scrollToSection(id) {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }
</script>

<nav>
  <ul>
    {#each sections as section}
      <li>
        <button on:click={() => scrollToSection(section.id)}>
          {section.title}
        </button>
      </li>
    {/each}
  </ul>
</nav>

<style>
  nav {
    background-color: transparent;
    width: 200px;
    height: 100%;
    padding: 1rem;
    position: fixed
  }

  ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  li {
    margin-bottom: 1rem;
  }

  button {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1rem;
    text-align: left;
    padding: 0.5rem;
    width: 100%;
  }

  button:hover {
    background-color: transparent;
    font-style: oblique;
  }
</style>
