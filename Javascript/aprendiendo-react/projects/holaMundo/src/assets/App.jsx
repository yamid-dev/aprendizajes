import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
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
        }
    ]

    return(
        <section className='App'>
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