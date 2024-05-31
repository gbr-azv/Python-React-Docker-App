import './Slider.css'
import Categories from '../Categories';

export const Slider = () => {

    return (
        <div className="slider">
            <Categories id="hamburgueres" />
            <Categories id="massas" />
            <Categories id="sushi" />
            <Categories id="drinks" />
        </div> 
    );
}
