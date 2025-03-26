<!-- Taken from https://svelte.dev/tutorial/kit/layout-data-->
<script>
	let { data } = $props();
</script>

<div class="container">
	<h1>blog</h1>

	<ul>
		{#each data.summaries as { slug, title }}
			<li><a href="/blog/{slug}">{title}</a></li>
		{/each}
	</ul>
</div>

<style>
	.container {
		padding: 3rem 0 5rem 5rem;
	}
</style>
