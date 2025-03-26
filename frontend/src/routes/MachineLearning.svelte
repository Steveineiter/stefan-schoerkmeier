<!--Taken from https://svelte.dev/tutorial/svelte/actions, improved with Claude Sonnet 3.7 and myself. -->
<script>
	import {predictNumber} from "$lib/services/mlService.js";
	import {convertDictTo2DListWithValues, convertToGrayscale, resizeImage} from "./imageManipulation.js";

	let { color, size } = $props();

	let canvas = $state();
	let context = $state();
	let coords = $state();
	let prediction = $state()



	$effect(() => {
		context = canvas.getContext('2d');

		// Set fixed dimensions instead of using window size
		canvas.width = 28;
		canvas.height = 28;

		drawBackground()

		return () => {};
	});

	function clearCanvas() {
		if (context) {
			context.clearRect(0, 0, canvas.width, canvas.height);
			drawBackground()
		}
	}

	function drawBackground() {
		context.fillStyle = "black";
		context.fillRect(0, 0, canvas.width, canvas.height)
	}

	async function recognizeNumber() {
    try {
      // Get canvas data as base64 string
      const pixels = context.getImageData(0, 0, canvas.width, canvas.height).data;
	  console.log(pixels)
	  const grayscalePixels = convertToGrayscale(pixels, canvas.width, canvas.height);
	  // const resizedPixels = resizeImage(grayscalePixels, canvas.width, canvas.height, 28, 28)
      const input = convertDictTo2DListWithValues(grayscalePixels)

      // Call the prediction service
      const response = await predictNumber(input);
	  prediction = response.prediction
    } catch (error) {
      console.error('Error recognizing number:', error);
      alert('Failed to recognize number');
    }
  }


</script>
<p>TODO write about machine learning</p>
<div class="canvas-container">
	<canvas
		bind:this={canvas}
		onpointerdown={(e) => {
			// Use clientX/Y relative to canvas position
			const rect = canvas.getBoundingClientRect();
			coords = {
				x: e.clientX - rect.left,
				y: e.clientY - rect.top
			};

			context.fillStyle = color;
			context.beginPath();
			context.arc(coords.x * (28 / rect.width), coords.y * (28 / rect.height), size / 2, 0, 2 * Math.PI);
			context.fill();
		}}
		onpointerleave={() => {
			coords = null;
		}}
		onpointermove={(e) => {
			if (!coords) return;

			const previous = coords;

			// Use clientX/Y relative to canvas position
			const rect = canvas.getBoundingClientRect();
			coords = {
				x: e.clientX - rect.left,
				y: e.clientY - rect.top
			};

			if (e.buttons === 1) {
				e.preventDefault();

				context.strokeStyle = color;
				context.lineWidth = size;
				context.lineCap = 'round';
				context.beginPath();
				context.moveTo(previous.x * (28 / rect.width), previous.y * (28 / rect.height));
				context.lineTo(coords.x * (28 / rect.width), coords.y * (28 / rect.height));
				context.stroke();
			}
		}}
	></canvas>

	{#if coords}
		<div
			class="preview"
			style="--color: {color}; --size: {size}px; --x: {coords.x}px; --y: {coords.y}px"
		></div>
	{/if}
	<div class="button-container">
	<button class="predict-button" onclick={recognizeNumber}>
	  Recognize Number
	</button>
	  <button class="reset-button" onclick={clearCanvas}>
		Reset Canvas
	  </button>
	</div>
	<div class="prediction-result">
		<h3>Recognized number: {prediction}</h3>
	</div>
	<div>
		<p>TODO create visualization & talk about MNIST data and why this is interesting to see (for such a "easy" problem
		we need so many neurons - imaging with real image data! :o cool)</p>
	</div>
</div>




<style>
	.canvas-container {
		position: relative;
		width: 500px;
		height: 500px;
	}

	canvas {
		width: 100%;
		height: 100%;
		border: 1px solid #000000;
		image-rendering: pixelated;
	}

	.preview {
		/*position: absolute;*/
		left: var(--x);
		top: var(--y);
		width: var(--size);
		height: var(--size);
		transform: translate(-50%, -50%);
		background: var(--color);
		border-radius: 50%;
		opacity: 0.5;
		pointer-events: none;
	}

	.button-container {
		display: flex;
		gap: 200px;
		margin-top: 10px;
		justify-content: flex-end
	}

	.reset-button, .predict-button {
		padding: 8px 16px;
		font-size: 16px;
		background-color: #000000;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	.prediction-result {
    	text-align: left;
	}


	.reset-button:hover {
		background-color: #000000;
	}
</style>
