// -*- web -*-
//
// michael a.g. aïvázis
// orthologue
// (c) 1998-2017 all rights reserved
//

// get the colors
import { wheel, semantic } from 'palette'

// publish
export default {
    // the style of the enclosing tag
    header: {
        position: "fixed",
        top: "0",
        left: "0",
        right: "0",
        zIndex: "9999",
        margin: "0em",
        padding: "0em",
        backgroundColor: wheel.chalk,
    },

    bar: {
        height: "1.5em",
        margin: "0.0em 2.0em 0.0em 2.0em",
        padding: "1.0em 2.0em 1.0em 2.0em",

        color: wheel.steel,
        borderBottom: `1px solid ${wheel.soapstone}`,
    },

    // navigation
    nav: {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",

        fontSize: "60%",
        whiteSpace: "nowrap",
    },

    // the logo: a link back to the home page
    logo: {
        height: "2.5em",
    },

    // other links
    link: {
        marginLeft: "0.5em",
        marginRight: "0.5em",
        paddingLeft: "0.5em",
        paddingRight: "0.5em",
        textTransform: "lowercase",
    },
}

// end of file
