<!-- Taken from https://svelte.dev/tutorial/kit/layout-data-->
<script>
	let { data } = $props();
</script>

<h1>{data.post.title}</h1>
<div>{@html data.post.content}</div>