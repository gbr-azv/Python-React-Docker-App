import './LogonButtons.css';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

export const LogonButtons = ({ hoverColor, icon, message }) => {

    return (
        <buttton className={`logon-button ${hoverColor}`} type='submit'>
            <FontAwesomeIcon icon={icon} className='icons'/>
            {message}
        </buttton>
    );
}
