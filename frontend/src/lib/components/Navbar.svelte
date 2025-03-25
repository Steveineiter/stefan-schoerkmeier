<script>
  // Define your sections
  const sections = [
    { id: 'section1', label: 'Section 1' },
    { id: 'section2', label: 'Section 2' },
    // { id: 'section3', label: 'Section 3' },
  ];

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
          {section.label}
        </button>
      </li>
    {/each}
  </ul>
</nav>

<style>
  nav {
    background-color: #f5f5f5;
    width: 200px;
    height: 100%;
    padding: 1rem;
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
    background-color: #e0e0e0;
  }
</style>
