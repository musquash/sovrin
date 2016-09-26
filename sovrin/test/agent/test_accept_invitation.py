from plenum.common.types import f
from plenum.test.eventually import eventually
from sovrin.agent.msg_types import MSG_TYPE_ACCEPT_INVITE
from sovrin.test.agent.helper import ensureAgentsConnected


def testFaberCreateLink(faberLinkAdded):
    pass


def testAcceptInvitation(faberIsRunning, faberLinkAdded, faberAdded,
                         aliceIsRunning, emptyLooper):
    """
    Faber creates a Link object, generates a link invitation file.
    Start FaberAgent
    Start AliceAgent and send a ACCEPT_INVITE to FaberAgent.
    """
    faber, fwallet = faberIsRunning
    alice, awallet = aliceIsRunning
    ensureAgentsConnected(emptyLooper, alice, faber)
    msg = {
        'type': MSG_TYPE_ACCEPT_INVITE,
        f.IDENTIFIER.nm: awallet.defaultId,
        'nonce': faberLinkAdded.nonce,
        f.SIG.nm: 'dsd'
    }
    alice.sendMessage(msg, faber.endpoint.name)

    def chk():
        assert faberLinkAdded.remoteIdentifier == awallet.defaultId
        assert faberLinkAdded.remoteEndPoint[1] == alice.endpoint.ha[1]
        # TODO: need to check remote identifier

    emptyLooper.run(eventually(chk))


def testAddClaimDef():
    pass


def testAddIssuerKeys():
    pass
