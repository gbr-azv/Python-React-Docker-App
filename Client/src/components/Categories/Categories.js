import './Categories.css'

import { useNavigate } from 'react-router-dom';

export const Categories = (props) => {

    const navigate = useNavigate();

    const navigateTo = () => {
        const searchParams = new URLSearchParams({ search : props.id });
        navigate(`/cardapio?${searchParams.toString()}`);
    }

    return (
        <div className="card" onClick={navigateTo}>
            <div className={props.id}></div>
            <div className="gradient"></div>
            <p className="title">{props.id}</p>
        </div>
    );
}
