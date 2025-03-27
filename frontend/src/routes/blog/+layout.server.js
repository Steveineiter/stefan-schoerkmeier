// // Taken from https://svelte.dev/tutorial/kit/layout-data
import { posts } from '$lib/text-data/blog-posts.js';

export function load() {
	return {
		summaries: posts.map((post) => ({
			slug: post.slug,
			title: post.title
		}))
	};
}
