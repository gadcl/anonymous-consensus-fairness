#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Build a block by the txs with minimum hash value
"""
def buildGoodEblock(node, numTxInBlock, termNum = 0):
    # ascending sort by hash
    sortedEblock = sorted(node.epool, key=lambda tx: tx.sha256ToInt("%s" % (termNum)))
    block = sortedEblock[:numTxInBlock]
    return block


"""
Build a block by the using b (num of txs in a block) different hash functions
and taking the txs that minimize each hash
"""
def buildGoodEblockMultipleHashFunc(node, numTxInBlock):
    
    # TODO finish this procedure
    for i in range(numTxInBlock):
        # ascending sort by hash
        sortedEpool = sorted(node.epool, \
                              key=lambda tx: tx.sha256ToInt("%s" % (i)))
        
    
    block = sortedEpool[:numTxInBlock]
    return block


"""
Build a block by taking txs with hash value lower than some threshold
"""
def buildGoodEblockConstThreshold(node, numTxInBlock, threshold):
    
    epool = node.epool
    block = []
    blockSize = 0
    
    for tx in epool:
        if tx.hashInt < threshold:
            block.append(tx)
            blockSize += 1
        if blockSize >= numTxInBlock:
            break
    
    return block
