<!-- Taken from https://svelte.dev/tutorial/kit/layout-data-->
<script>
	let { data } = $props();
</script>

<h1>{data.post.title}</h1>
<div class="text-content">{@html data.post.content}</div>

<style>
    .text-content {
        flex: 1;
        min-width: 300px;
        max-width: 65ch;
    }
</style>
