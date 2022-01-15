<script>
  import TextComp from '$lib/comps/textcomp.svelte';
  import CommentComp from '$lib/comps/commentcomp.svelte';
  import { fade } from 'svelte/transition';

  let show = true;
  let show2 = false;

  let showit = () => {
    if (!show) {
      show = true;
      show2 = false;
    } else {
      show = false;
      show2 = true;
    }
  };

  let showit2 = () => {
    if (!show2) {
      show2 = true;
      show = false;
    } else {
      show2 = false;
      show = true;
    }
  };
</script>

<div>
  <svg
    on:click={showit}
    xmlns="http://www.w3.org/2000/svg"
    width="16"
    height="16"
    fill="currentColor"
    class="bi bi-chat-square-dots"
    viewBox="0 0 16 16"
  >
    <path
      d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1h-2.5a2 2 0 0 0-1.6.8L8 14.333 6.1 11.8a2 2 0 0 0-1.6-.8H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2.5a1 1 0 0 1 .8.4l1.9 2.533a1 1 0 0 0 1.6 0l1.9-2.533a1 1 0 0 1 .8-.4H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
    />
    <path
      d="M5 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"
    />
  </svg>

  <svg
    id="one"
    on:click={showit2}
    xmlns="http://www.w3.org/2000/svg"
    width="16"
    height="16"
    fill="currentColor"
    class="bi bi-chat-square-text"
    viewBox="0 0 16 16"
  >
    <path
      d="M14 1a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1h-2.5a2 2 0 0 0-1.6.8L8 14.333 6.1 11.8a2 2 0 0 0-1.6-.8H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2.5a1 1 0 0 1 .8.4l1.9 2.533a1 1 0 0 0 1.6 0l1.9-2.533a1 1 0 0 1 .8-.4H14a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
    />
    <path
      d="M3 3.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 6a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 6zm0 2.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z"
    />
  </svg>
</div>

{#if show}
<div transition:fade ><TextComp /></div>
  
{:else}
  <div transition:fade />
{/if}

{#if show2}

<div transition:fade ><CommentComp /></div>
  
{:else}
  <div transition:fade />
{/if}

<style>
  #one {
    float: right;
  }

  svg {
    width: 4em;
    height: 4em;
  }
</style>
