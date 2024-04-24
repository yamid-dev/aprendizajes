import Carousel from 'react-bootstrap/Carousel';
import ExampleCarouselImage from './ExampleCarouselImage';
import { TwitterFollowCard } from './TwitterFolloCard'

export function UncontrolledExample() {
  return (
    <Carousel>
      <Carousel.Item>
        <ExampleCarouselImage src='https://unavatar.io/yamid-dev' alt="Yamid Dev"/>
        <Carousel.Caption>
          <h3>Yamid Dev</h3>
          <p>Software Developer Full Stack Colombiano.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <ExampleCarouselImage src='https://unavatar.io/midudev' alt="Midudev" />
        <Carousel.Caption>
          <h3>Midudev</h3>
          <p>Git Star y Software Developer Full Stack Español.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <ExampleCarouselImage src='https://unavatar.io/mouredev' alt="MoureDev"/>
        <Carousel.Caption>
          <h3>Mouredev</h3>
          <p>Git Star y Software Developer Full Stack Español.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <ExampleCarouselImage src='https://unavatar.io/soyDalto' alt="SoyDalto"/>
        <Carousel.Caption>
          <h3>SoyDalto</h3>
          <p>Software Developer Full Stack Argentino.</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <ExampleCarouselImage src='https://unavatar.io/Maria' alt="Maria"/>
        <Carousel.Caption>
          <h3>Maria</h3>
          <p>
            Software Developer Full Stack
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
}