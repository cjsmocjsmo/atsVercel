<script>
  import Header from '$lib/header/Header.svelte';
  import '../app.css';

</script>

<h1>above nav bar</h1>
<Header />

<main>
  <slot />
</main>

<footer>
  <h1>360 516 8933</h1>
  <h1>did it work</h1>
</footer>

<style>
  @import url('https://fonts.googleapis.com/css?family=Roboto:700');

  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    width: 100%;
    max-width: 1024px;
    margin: 0 auto;
    box-sizing: border-box;
  }

  footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px;
  }

  @media (min-width: 480px) {
    footer {
      padding: 40px 0;
    }
  }
</style>
