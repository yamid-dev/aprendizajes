import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
import { UncontrolledExample } from './Carrusel'

export function App () {
    
    const users= [
        {
            userName: 'yamid-dev',
            name: 'Yamid Horacio Rodríguez',
            isFollowing: true
        },
        {
            userName: 'midudev',
            name: 'Miguel Ángel Durán',
            isFollowing: false
        },
        {   
            userName: 'mouredev',
            name: 'Brais Moure',
            isFollowing: true
        },
        {   
            userName: 'SoyDalto',
            name: 'Lucas Dalto',
            isFollowing: false
        },
        {   
            userName: 'Maria',
            name: 'Maria Pastrana',
            isFollowing: true
        }
    ]

    return(  
        <section className='App'>
            <UncontrolledExample></UncontrolledExample>
            {   
                users.map(({userName,name,isFollowing})=>(
                        <React.Fragment>
                            <TwitterFollowCard 
                            key={userName}
                            userName={userName}
                            initialIsFollowing = {isFollowing}>
                                {name}
                            </TwitterFollowCard>
                        </React.Fragment>
                    ))
            }
            
        </section>
    )
}