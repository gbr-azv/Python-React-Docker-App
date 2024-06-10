import Slider from '../components/Slider';
import Banner from '../components/Banner';
import Wrapper from '../components/Wrapper';
import Card from '../components/Card';

function Home() {
  return (
    <div className="App">
      <Slider />
      <Banner />
      <Wrapper>
        <Card
          header3="Ainda não tem cadastro?"
          header1="Cadastre-se Agora"
          paragraph="E obtenha 10% de desconto na primeira compra!"
          button="Cadastrar"
        >
        </Card>
        <Card
          header3="Promoções rolando no App!"
          header1="Coma bem e barato"
          paragraph="Produtos com até 20% OFF!"
          button="Conferir"
        >
        </Card>
      </Wrapper>
    </div>
  );
}

export default Home;
