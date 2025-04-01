<!--Taken from https://svelte.dev/tutorial/svelte/actions, improved with Claude Sonnet 3.7 and myself. -->
<script>
	import { on } from "svelte/events"
	import {predictNumber} from "$lib/services/mlService.js";
	import {convertDictTo2DListWithValues, convertToGrayscale, resizeImage} from "../../utility/imageManipulation.js";

	let { title } = $props();


	let DRAWING_COLOR = "white";
	let DRAWING_SIZE = 1;

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
<h2>{@html title}</h2>
<p>
	Machine learning (often referred to as Artificial Intelligence (AI) or <i>Künstliche Intelligenz</i> (KI) in German) has
	many use cases. Currently, it is widely recognized for its applications in large language models (LLMs) like ChatGPT.
	<br><br>
	This makes sense because its performance in knowledge work is amazing. Personally, I use it more often than Google,
	as the results are, on average, better than reading a random blog post about a topic.
	<br><br>
	However, besides LLMs, we should not forget the other great applications of machine learning. One of these is
	<b>pattern recognition and prediction.</b> Give it a try below :)
</p>
<div class="canvas-container">
	<canvas
		bind:this={canvas}
		onpointerdown={(e) => {
			e.preventDefault();
			// Use clientX/Y relative to canvas position
			const rect = canvas.getBoundingClientRect();
			coords = {
				x: e.clientX - rect.left,
				y: e.clientY - rect.top
			};

			context.fillStyle = DRAWING_COLOR;
			context.beginPath();
			context.arc(coords.x * (28 / rect.width), coords.y * (28 / rect.height), DRAWING_SIZE / 2, 0, 2 * Math.PI);
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

			if (e.buttons === 1 || e.pointerType === "touch") {
				e.preventDefault();

				context.strokeStyle = DRAWING_COLOR;
				context.lineWidth = DRAWING_SIZE;
				context.lineCap = 'round';
				context.beginPath();
				context.moveTo(previous.x * (28 / rect.width), previous.y * (28 / rect.height));
				context.lineTo(coords.x * (28 / rect.width), coords.y * (28 / rect.height));
				context.stroke();
			}
		}}


	></canvas>

	<div class="button-container">
	<button class="predict-button" onclick={recognizeNumber}>
	  Recognize Number
	</button>
	  <button class="reset-button" onclick={clearCanvas}>
		Reset Canvas
	  </button>
	</div>
	<div class="prediction-result">
		<h3>Recognized number (0-9): {prediction}</h3>
	</div>
</div>

<div>
	<p>
		If you are wondering why it just won't correctly predict your perfect 1 (I did, at least),
		that’s because of a fundamental rule of machine learning: It’s <b>all about the data</b>. In the
		<a href="https://en.wikipedia.org/wiki/MNIST_database" target="_blank" rel="noopener noreferrer">
			MNIST dataset
		</a>, the number 1 is often written as a |, so our poor model never really had a chance to correctly recognize it...
	</p>
</div>
<!--	<div>-->
<!--		<p>TODO create visualization & talk about MNIST data and why this is interesting to see (for such a "easy" problem-->
<!--		we need so many neurons - imaging with real image data! :o cool)</p>-->
<!--		Probably create a sectoin for each of those-->
<!--		<h2>TODO doodle to image</h2>-->
<!--		<h2>TODO LLM to collect feedback</h2>-->
<!--		<h2>TODO innovation / use prediciton for side navigation</h2>-->
<!--	</div>-->

<style>
	h2 {
		text-align: right;
	}
	p {
		text-align: left;
		margin-left: auto;
		margin-right: 0;
		flex: 1;
		min-width: 300px;
		max-width: 65ch;
	}

	.canvas-container {
		position: relative;
		width: 500px;
		height: 500px;
		margin: 0 100px 0 auto;
		display: flex;
		flex-direction: column;
	}

	canvas {
		width: 100%;
		height: 100%;
		border: 1px solid #000000;
		image-rendering: pixelated;
	}

	.button-container {
		display: flex;
		gap: 200px;
		margin-top: 10px;
		justify-content: flex-end;
	}

	.reset-button,
	.predict-button {
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
  /********************************* Mobile screen *********************************/
	@media (max-width: 768px) {
		.canvas-container {
			width: 100%;
			height: auto;
			flex-direction: column;
			align-items: center;
		}

		canvas {
			width: 80%;
			height: auto;
		}

		.button-container {
			flex-direction: column;
			gap: 10px;
			justify-content: center;
			align-items: center;
		}

		.reset-button,
		.predict-button {
			width: 100%;
			font-size: 14px;
		}
	}
</style>