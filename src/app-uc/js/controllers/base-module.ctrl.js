export default (ngModule) => {

  ngModule.controller('BaseModuleCtrl', ['$scope', ($scope) => {
    console.warn('基本个人中心根模型信息');
  }]);


  // Singleton example.
  const singleton = (() => {

    // Instance stores  a referene to the Singleton.
    let instance;

    function init() {

      function privateMethod() {
        console.warn('this is private methoe.');
      }

      const privateVariable = 'this is private variable.';
      const privateNumber = Math.random();

      return {
        publicMethod: () => {
          console.warn('this is public method.');
        },
        publicProperty: 'this is public property.',
        getRandomNumber: () => privateNumber
      };
    }

    return {
      initInstance: () => {
        if(!instance) {
          instance = init();
        }
        return instance;
      }
    };

  })();

  const singleton1 = singleton.initInstance();
  const singleton2 = singleton.initInstance();

  console.warn('singleton test: ', singleton1.getRandomNumber === singleton2.getRandomNumber);
};
