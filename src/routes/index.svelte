<!-- <div id="IFrame">
	<iframe 
		
	  	width="990" 
		height="560" 
		src="https://www.youtube.com/embed/okVkEfmoTTA" 
		title="YouTube video player" 
		frameborder="0" 
		allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
		allowfullscreen>
	</iframe>
  </div> -->
<script>
	// import Swiper core and required modules
	import { Navigation, Pagination, Scrollbar, A11y, Lazy } from 'swiper';

	import { Swiper, SwiperSlide } from 'swiper/svelte';

	// Import Swiper styles
	import 'swiper/css';
	import 'swiper/css/navigation';
	import 'swiper/css/pagination';
	import 'swiper/css/scrollbar';
	// import './styles.css';
	import pic1 from '$lib/images/pic1.webp';
	import pic2 from '$lib/images/pic2.webp';
	import pic3 from '$lib/images/pic3.webp';
	import pic4 from '$lib/images/pic4.webp';
	import pic5 from '$lib/images/pic5.webp';
	import pic6 from '$lib/images/pic6.webp';
	import pic7 from '$lib/images/pic7.webp';
	import pic8 from '$lib/images/pic8.webp';
	import pic9 from '$lib/images/pic9.webp';
	import pic10 from '$lib/images/pic10.webp';


</script>

<h1>Alpha Tree Service</h1>
<h2>360 516 8933</h2>

<Swiper
	modules={[Navigation, Pagination, Scrollbar, A11y]}
	spaceBetween={10}
	slidesPerView={2}
	navigation
	pagination={{ clickable: true }}
	scrollbar={{ draggable: true }}
	on:slideChange={() => console.log('slide change')}
	on:swiper={(e) => console.log(e.detail[0])}
>
	<SwiperSlide><img src={pic1} alt="fuckit" /></SwiperSlide>
		
		
	<SwiperSlide><img src={pic2} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic3} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic4} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic5} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic6} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic7} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic8} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic9} alt="fuckit" /></SwiperSlide>
	<SwiperSlide><img src={pic10} alt="fuckit" /></SwiperSlide>

	...
</Swiper>


<div class="box1">

<div id="IFrame">
	<iframe 
		
	  	width="490" 
		height="280" 
		src="https://www.youtube.com/embed/okVkEfmoTTA" 
		title="YouTube video player" 
		frameborder="0" 
		allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
		allowfullscreen>
	</iframe>
  </div>

  <p>I contacted Curtis about removing several, dangerous trees on my property. 
	He showed up on time and ready to work. He did exactly what I expected him to do. 
	He does exceptional work. I will continue to call Curtis when I need a tree removed. 
	I would highly recommend Alphatree. Dan
	do1058</p>

  </div>

  <div class="box2">
  <p>Curtis and crew took down an 80’ fir near a fence and house. NO DAMAGE!!! 
	Cleanup was thorough and they cut the rounds into 14” rounds for later splitting. 
	Crew had a great attitude. Will use them again.
	- Kurt R</p>

  <div id="IFrame2">
	<iframe 
		width="490" 
		height="280" 
		src="https://www.youtube.com/embed/MAhLq6x6jOM" 
		title="YouTube video player" 
		frameborder="0" 
		allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
		allowfullscreen>
	</iframe>
  </div>
</div>
<!-- <script>
  // Import Swiper Svelte components
  import { Swiper, SwiperSlide } from 'swiper/svelte';

  // Import Swiper styles
  import 'swiper/css';
</script>


<Swiper
    spaceBetween={20}
    slidesPerView={3}
	navigation
    on:slideChange={() => console.log('slide change')}
    on:swiper={(e) => console.log(e.detail[0])}
  >
    <SwiperSlide>Slide 1</SwiperSlide>
    <SwiperSlide>Slide 2</SwiperSlide>
    <SwiperSlide>Slide 3</SwiperSlide>
    <SwiperSlide>Slide 4</SwiperSlide>
    ...
  </Swiper> -->
<style>
	h2 {
		text-align: center;
	}

	#IFrame {
		margin-top: 0.5em;
	}

	.box1 {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}
	
	.box2 {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}



	@media (max-width: 450px) {
		iframe {
			width: 370px;
			height: 187px;
		}

		.box1, .box2 {
			flex-direction: column;
		}
	}

	/* .swiper {
		width: 100%;
		height: 100%;
		}

	.swiper-slide {
		background-position: center;
		background-size: cover;
	}

	.swiper-slide img {
		display: block;
		width: 100%;
	} */

</style>
