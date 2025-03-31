<script>
  let { title } = $props();
</script>

<div class="about-container">
  <div class="text-content">
    <h2>{title}</h2>
    <p>I'm Stefan, a computer scientist crafting creative, efficient and innovative solutions. I stand for</p>

    <ul class="bullet-points">
      <li>focus on quality</li>
      <li>great communication</li>
      <li>cutting edge technology</li>
      <li>planning & time management</li>
    </ul>

    <p>I love to <strong>implement modern solutions</strong> and find ways how we can solve real world problems with innovative approaches.</p>

    <p>I think there is a lot of potential in bringing <strong>machine learning</strong> to your business and everyday life.</p>
  </div>
  <div class="image-content">
    <img src="/images/portrait.png" alt="My Portrait">
  </div>
</div>


<style>
h2 {
  margin-top: 0;
}

img {
  max-width: 100%;
  height: auto;
  border-radius: 25px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.about-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  width: 100%;
  padding-top: 2rem;
}

.text-content {
  flex: 1;
  min-width: 300px;
  max-width: 65ch; /* Optimal reading width */
}

.image-content {
  flex: 1;
  min-width: 300px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.bullet-points {
  list-style-type: none;
  padding-left: 1.5rem;
  margin: 1rem 0;
}

.bullet-points li {
  position: relative;
  padding-left: 1rem;
  margin-bottom: 0.5rem;
}

.bullet-points li::before {
  content: "•";
  position: absolute;
  left: -1rem;
}


 /********************************* Mobile screen*********************************/
@media (max-width: 768px) {
  .about-container {
    flex-direction: column-reverse;
  }

  .image-content {
    margin-bottom: 2rem;
  }
}

 /********************************* Desktop and larger screens *********************************/
@media (min-width: 769px) {
  .about-container {
    flex-direction: row;
  }
}
</style>