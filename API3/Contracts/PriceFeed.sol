pragma solidity 0.8.22;

import "@api3/contracts/api3-server-v1/proxies/interfaces/IProxy.sol";

contract PriceFeed {

    address public feed1;
    address public feed2;

    constructor(){}

    function setupFeed1(address _priceFeed) external {
        feed1 = _priceFeed;
    }

    function setupFeed2(address _priceFeed) external {
        feed2 = _priceFeed;
    }

    function readDataFeed1() public view returns (uint256, uint256){
        (int224 value, uint256 timestamp) = IProxy(feed1).read();
        uint256 price = uint224(value);
        return (price, timestamp);
    }

    function readDataFeed2() public view returns (uint256, uint256){
        (int224 value, uint256 timestamp) = IProxy(feed2).read();
        uint256 price = uint224(value);
        return (price, timestamp);
    }

}

// ETH Usd feed: 0xb392dD92571D2d8695759fC86aB01bE993738795
// API3 Usd feed: 0x387Ee90D1D51898b2D870A86b02e3d1D43758d30