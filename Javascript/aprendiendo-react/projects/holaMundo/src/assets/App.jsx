import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {
    return(
        <React.Fragment>
            <TwitterFollowCard />
            <TwitterFollowCard />
            <TwitterFollowCard />
            <TwitterFollowCard />
        </React.Fragment>
    )
}