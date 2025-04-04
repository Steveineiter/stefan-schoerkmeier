import { describe, test, expect } from 'vitest';
import '@testing-library/jest-dom/vitest';
import { render, screen } from '@testing-library/svelte';
import Page from '../../src/routes/+page.svelte';

describe('/+page.svelte', () => {
	test('should render navigation', () => {
		render(Page);
		expect(screen.getByRole('navigation')).toBeInTheDocument();
	});
});
