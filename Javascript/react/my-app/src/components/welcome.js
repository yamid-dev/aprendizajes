export default function welcome(props){
    console.log(props)
    const { message } = props;
    const { name } = props;
    return(<p>{message} {name} desde la funcion Welcome :3</p>)
}