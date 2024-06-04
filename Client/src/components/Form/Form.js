import './Form.css';

export const Form = ({ children, onSubmit }) => {

    return (
        <form className='form' onSubmit={onSubmit} >
            <div className='outter-div'>
                { children }    
            </div> 
        </form>
    );
}
