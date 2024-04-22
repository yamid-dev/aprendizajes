import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {
    return(
        <>
            <TwitterFollowCard userName="yamiddev" name="Yamid Horacio Rodríguez"/>
            <TwitterFollowCard userName="midudev" name="Mauricio Rozo" />
            <TwitterFollowCard userName="christian" name="Christian Martinez"/>
            <TwitterFollowCard userName="valexd" name="Valentina Velandia"/>
        </>
    )
}