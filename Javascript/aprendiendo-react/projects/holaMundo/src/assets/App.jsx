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
            isFollowing: true
        },
        {   
            userName: 'mouredev',
            name: 'Brais Moure',
            isFollowing: true
        },
        {   
            userName: 'SoyDalto',
            name: 'Lucas Dalto',
            isFollowing: true
        }
    ]

    return(
        <section className='App'>
            {
                users.map(user =>{
                    const {userName,name,isFollowing} = user
                    return(
                        <React.Fragment>
                            <TwitterFollowCard 
                            userName={userName}
                            initialIsFollowing = {isFollowing}>
                                {name}
                            </TwitterFollowCard>
                        </React.Fragment>
                    )
                })
            }    
        </section>
    )
}