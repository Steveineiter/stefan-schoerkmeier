// Taken from https://svelte.dev/tutorial/kit/layout-data
import { error } from '@sveltejs/kit';
import { posts } from '$lib/text-data/blog-posts.js';

export function load({ params }) {
	const post = posts.find((post) => post.slug === params.slug);

	if (!post) error(404);

	return {
		post
	};
}
