<script>
  import Icon from './Icons.svelte';
  import {typewriter} from '$lib/utility/transitions.js'

  const myName = "Stefan Schörkmeier";
  const socials = [
    {
      name: "Email",
      url: "mailto:s.schoerkmeier+business@gmail.com",
      icon: "email"
    },
    {
      name: "LinkedIn",
      url: "https://linkedin.com/in/stefan-schörkmeier",
      icon: "linkedin"
    },
    {
      name: "GitHub",
      url: "https://github.com/steveineiter",
      icon: "github"
    },
  ];

  // ===================================================================
  let messages = ["Machine Learning Engineer", "Software Developer", ];
  let currentIndex = $state(0);

  $effect(() => {
    const interval = setInterval(() => {
      currentIndex += 1;
      currentIndex %= messages.length;
    }, 5000);
    return () => {
      clearInterval(interval);
    };
  });
</script>

<header>
  <div class="header-content">
    <a href="/" data-sveltekit-preload-data>
      <h1>{myName}</h1>
    </a>
    {#key currentIndex}
	<h2 in:typewriter={{ speed: 1.5 }}>
		{messages[currentIndex] || ''}
	</h2>
    {/key}
    <br>

    <div class="social-links">
      {#each socials as social}
        <a href={social.url} target="_blank" rel="noopener noreferrer">
          <Icon name={social.icon} width="16px" height="16px" fill="white" class="icon" />
          <span>{social.name}</span>
        </a>
      {/each}
      <a href="/blog" >
        <Icon name="blog" width="16px" height="16px" fill="white" class="icon" />
        <span>Blog</span>
      </a>

    </div>
  </div>
</header>


<style>
  header {
    background-color: #000000;
    color: white;
    border-bottom: 2px solid #ffffff;
    padding: 3rem;
    position: sticky;
    top: 0;
    width: 100%;
    z-index: 100;
    box-sizing: border-box;
  }

  h1 {
    margin: 0;
    font-size: xxx-large;
    cursor:pointer;
  }

  h2 {
    margin:0;
    min-height: 1.5em
  }

  a {
    text-decoration: none;
    color: inherit
  }

  .social-links {
    display: flex;
    gap: 20px;
    margin-top: 0.5rem;
  }

  .header-content {
    max-width: 1000px;
    margin: 0 auto;
  }
  .social-links a {
    display: flex;
    align-items: center;
    gap: 5px;
    color: white;
    text-decoration: none;
    transition: opacity 0.3s ease;
  }

  .social-links a:hover {
    opacity: 0.8;
  }

  svg {
    vertical-align: middle;
  }

   @media (max-width: 1024px) {
     header {
       padding: 1rem 0 2rem 0.2rem;
     }

     h2 {
      min-height: 2.5em
     }
   }
</style>
