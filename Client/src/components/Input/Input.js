import './Input.css';

export const Input = (props) => {

    return (
        <div className='input-container'>
            <label className='label' htmlFor={props.for}>{props.label}</label>
            <input
                className='input' 
                type={props.type}
                placeholder={props.placeholder}
            />
        </div>
    );
}
