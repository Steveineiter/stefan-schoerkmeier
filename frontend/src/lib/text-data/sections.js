import AboutMe from '$lib/components/sections/AboutMe.svelte';
import MachineLearning from '$lib/components/sections/MachineLearning.svelte';
import Projects from '$lib/components/sections/Projects.svelte';
import Certificates from '$lib/components/sections/Certificates.svelte';
import Knowledge from '$lib/components/sections/Knowledge.svelte';

export const sections = [
  {
    id: "about",
    title: "About me",
    component: AboutMe,
  },
  {
    id: "ml",
    title: "Machine Learning",
    component: MachineLearning,
  },
  {
    id: "projects",
    title: "Projects",
    component: Projects
  },
  {
    id: "certificates",
    title: "Certificates",
    component: Certificates
  },
  {
    id: "knowledge",
    title: "Knowledge",
    component: Knowledge
  },
];