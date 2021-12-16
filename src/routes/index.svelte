<script>
  // import Swiper core and required modules
  import { Navigation, Pagination, Scrollbar, A11y, Lazy } from 'swiper';

  import { Swiper, SwiperSlide } from 'swiper/svelte';
  import Randomcommentcomp from '$lib/comps/randomcommentcomp.svelte';

  import 'swiper/css';
  import 'swiper/css/navigation';
  import 'swiper/css/pagination';
  import 'swiper/css/scrollbar';

  import pic1 from '$lib/images/caroselimages/20200703_122208_thumb.webp';
  import pic2 from '$lib/images/caroselimages/20200703_122216_thumb.webp';
  import pic3 from '$lib/images/caroselimages/20200703_122218_thumb.webp';
  import pic4 from '$lib/images/caroselimages/20200703_122219_thumb.webp';
  import pic5 from '$lib/images/caroselimages/20200703_122220_thumb.webp';
  import pic6 from '$lib/images/caroselimages/20200703_122229_thumb.webp';
  import pic7 from '$lib/images/caroselimages/20210918_105104_thumb.webp';
  import pic8 from '$lib/images/caroselimages/20210918_105122_thumb.webp';
  import pic9 from '$lib/images/caroselimages/20210918_105132_thumb.webp';
  import pic10 from '$lib/images/caroselimages/20210918_112452_thumb.webp';

  const c1 =
    'I contacted Curtis about removing several, dangerous trees on my property.';
  const c2 =
    '  He showed up on time and ready to work. He did exactly what I expected him';
  const c3 =
    ' to do. He does exceptional work. I will continue to call Curtis when I need';
  const c4 = ' a tree removed. I would highly recommend Alphatree. Dan do1058';
  const content = c1 + c2 + c3 + c4;

  const s1 =
    'Curtis and crew took down an 80’ fir near a fence and house. NO DAMAGE!!!';
  const s2 =
    '  Cleanup was thorough and they cut the rounds into 14” rounds for later';
  const s3 =
    ' splitting. Crew had a great attitude. Will use them again. - Kurt R';
  const content2 = s1 + s2 + s3;
</script>

<h1>360 516 8933</h1>

<Swiper
  modules={[Navigation, Pagination, Scrollbar, A11y]}
  spaceBetween={10}
  slidesPerView={3}
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
      allowfullscreen
    />
  </div>
  <Randomcommentcomp {content} />
</div>

<div class="box2">
  <Randomcommentcomp content={content2} />
  <div id="IFrame2">
    <iframe
      width="490"
      height="280"
      src="https://www.youtube.com/embed/MAhLq6x6jOM"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    />
  </div>
</div>

<style>
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

  @media (max-width: 531px) {
    iframe {
      width: 370px;
      height: 187px;
    }

    .box1,
    .box2 {
      flex-direction: column;
    }
  }

  @media (max-width: 365px) {
    iframe {
      width: 310px;
      height: 175px;
    }
  }
</style>
