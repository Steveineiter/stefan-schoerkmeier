// Taken from https://svelte.dev/tutorial/kit/layout-data
export const posts = [
	{
		slug: 'welcome',
		title: 'Code generation and problems I see for the future',
		content:
			'<p>According to CEOs of top AI companies a large amount of code will be written by AI. ' +
			'Anthropic CEO Dario Amodei mentioned that 90% of code in 2025 and 100% of code in 2025. ' +
			'</p>' +
			'<p>This might be the case, that we are at least working in a pair-progrmaming manner aka ' +
			'that the code is generated but there is a human in the loop. The <b>problem</b> I have seen from this ' +
			'project as example is, that LLMs are terrible with new technologies / frameworks. That makes sense ' +
			'since they simply don\'t have enough training data. </p>' +
			'<p>With the hype of LLMs replacing or enhancing many engineers, we most likely will mainly use old ' +
			'framworks where the LLMs can generate good code quality. But this is obviously a huge <b>secuirty issue</b> ' +
			'right? Imagine that 90% of the code will be with outdated versions with known security issues.</p>' +
			'<p>So I don\'t advice of not using those tools, but I do believe we have to keep such things in mind.</p>'
	},

	{
		slug: 'safety',
		title: 'placeholder 2',
		content:
			'<p>foo</p>'
	},

	{
		slug: 'cake',
		title: 'placeholder 3',
		content: "<p>bar</p>"
	}
];
