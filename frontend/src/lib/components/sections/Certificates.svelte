<script>
  let { title } = $props();
</script>

<div class="certificates-container">
  <div class="text-content">
    <h2>{title}</h2>
    <h3>Education</h3>
    <ul class="education-bullet-points">
      <li>Master of Science, Softwaredevelopement Management (Major: Machine Learning, Minor: Business Law), Graz univisity of technology, Graz, 2022-ongoing</li>
      <li>Bachelor of Science, Softwaredevelopement Management, Graz Univieristy of technology, Graz, 2018-2022</li>
    </ul>

    <h3>Kaggle (selection)</h3>
    <ul class="other-bullet-points">
      <li>Oxford english test</li>
    </ul>

    <h3>Udemy</h3>
    <ul class="other-bullet-points">
      <li>Oxford english test</li>
    </ul>

    <h3>Other</h3>
    <ul class="other-bullet-points">
      <li>Oxford english test</li>
    </ul>
  </div>
</div>


<style>
	h2 {
		text-align: right;
	}

	.certificates-container {
		text-align: left;
		margin-left: auto;
		margin-right: 0;
		flex: 1;
		min-width: 300px;
		max-width: 75ch;
	}

</style>