import '../styles/Logon.css';

import Form from '../components/Form';
import Input from '../components/Input';
import LogonButtons from '../components/LogonButtons';

import { faFacebook, faTwitter, faGoogle } from '@fortawesome/free-brands-svg-icons';
import { faPaperPlane  } from '@fortawesome/free-solid-svg-icons';

function Logon() {

  return (
    <Form>
      <div className='logon-inputs'>
        <Input type='text' placeholder='Digite seu nome completo...' htmlFor='username' label='Nome Completo' />
        <Input type='email' placeholder='Digite seu melhor e-mail...' htmlFor='email' label='E-mail' />
        <Input type='password' placeholder='Digite sua senha...' htmlFor='password' label='Senha' />
        <Input type='tel' placeholder='Digite seu melhor número de celular...' htmlFor='phone' label='Celular' />
        <Input type='text' placeholder='Digite seu endereço...' htmlFor='address' label='Endereço' />
      </div>
      <div className='logon-buttons'>
        <LogonButtons message='Finalizar Cadastro' hoverColor='email-hover' icon={faPaperPlane } />
        <p className='buttons-divisor'>Ou</p>
        <div className='oauth-buttons'>
          <LogonButtons message='Continuar com Google' hoverColor='google-hover' icon={faGoogle} />
          <LogonButtons message='Continuar com Facebook' hoverColor='fa-hover' icon={faFacebook} />
          <LogonButtons message='Continuar com Twitter' hoverColor='tt-hover' icon={faTwitter} />
        </div>
      </div>
    </Form>
  );
}

export default Logon;
