import * as common from './common'

export const commons = common
/**
 * 动态加载JS文件
 * @param {String} url
 */
export function loadScript (url, id) {
  // eslint-disable-next-line no-unused-vars
  return new Promise((resolve, reject) => {
    const script = document.createElement('script')
    script.type = 'text/javascript'
    if (script.readyState) {
      script.onreadystatechange = () => {
        if (script.readyState === 'loaded' || script.readyState === 'complete') {
          script.onreadystatechange = null
          resolve()
        }
      }
    } else {
      script.onload = () => {
        resolve()
      }
    }
    script.src = url
    // 规定是否对该资源文件异步加载
    script.async = false
    if (id) {
      script.id = id
    }
    document.body.insertAdjacentElement('beforeend', script)
  })
}

/**
 * 同步加载css文件
 */
export function loadCSS (url, id) {
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.type = 'text/css'
  link.href = url
  if (id) {
    link.id = id
  }
  document.querySelector('head').insertAdjacentElement('beforeend', link)
}

/**
 * 获取指定位数的用于唯一识别的字符串
 * @param {Number} decimal
 */
export function uuid (decimal) {
  const alps = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  const s = []
  for (let i = 0; i < decimal; i++) {
    s[i] = alps.substr(Math.floor(Math.random() * 62), 1)
  }
  return s.join('')
}

/**
 * 判断是否为数字
 * @param {*} value
 */
export function isNumber (value) {
  return Object.prototype.toString.call(value) === '[object Number]'
}

/**
 * 判断是否为字符串
 * @param {*} value
 */
export function isString (value) {
  return Object.prototype.toString.call(value) === '[object String]'
}

/**
 * 判断是否为数组
 * @param {*} value
 */
export function isArray (value) {
  return Object.prototype.toString.call(value) === '[object Array]'
}

/**
 * 判断是否为布尔类型
 * @param {*} value
 */
export function isBoolean (value) {
  return Object.prototype.toString.call(value) === '[object Boolean]'
}

/**
 * 判断是否为undefined
 * @param {*} value
 */
export function isUndefined (value) {
  return Object.prototype.toString.call(value) === '[object Undefined]'
}

/**
 * 判断是否为null
 * @param {*} value
 */
export function isNull (value) {
  return Object.prototype.toString.call(value) === '[object Null]'
}

/**
 * 判断是否为symbol
 * @param {*} value
 */
export function isSymbol (value) {
  return Object.prototype.toString.call(value) === '[object Symbol]'
}

/**
 * 判断是否为函数
 * @param {*} value
 */
export function isFunction (value) {
  return Object.prototype.toString.call(value) === '[object Function]'
}

/**
 * 判断是否为对象
 * @param {*} value
 */
export function isObject (value) {
  return (
    Object.prototype.toString.call(value) === '[object Object]' ||
    // if it isn't a primitive value, then it is a common object
    (!isNumber(value) &&
      !isString(value) &&
      !isBoolean(value) &&
      !isArray(value) &&
      !isNull(value) &&
      !isFunction(value) &&
      !isUndefined(value) &&
      !isSymbol(value)
    )
  )
}
